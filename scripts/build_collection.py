#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
从 MediaCrawler 抓取的知乎 JSON，生成「静水2008」的两个派生文件：
  1. 静水2008-知乎合集.md   —— 按时间排序的全文合集（含目录表）
  2. 原文索引.md            —— 按点赞排序的索引表（skill 内置）

用法：
  python3 build_collection.py [--json-dir PATH] [--out-collection PATH] [--out-index PATH]

默认路径指向本机的 MediaCrawler 输出与 jingshui 仓库位置，可按需覆盖。
"""
import argparse
import glob
import json
import os
import time

DEFAULT_JSON_DIR = "/Users/z/Documents/work/project/MediaCrawler/data/zhihu/json"
DEFAULT_OUT_COLLECTION = "/Users/z/Documents/work/project/MediaCrawler/data/zhihu/markdown/静水2008-知乎合集.md"
DEFAULT_OUT_INDEX = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "原文索引.md")

EXCERPT_LEN_COLLECTION = 30   # 合集里目录/标题的摘要长度
EXCERPT_LEN_INDEX = 38        # 原文索引里摘要的长度


def normalize(s: str) -> str:
    """去掉知乎 API desc 里残留的空格与换行。"""
    return (s or "").replace(" ", "").replace("\n", "").replace("\r", "").strip()


def excerpt(text: str, n: int) -> str:
    text = normalize(text)
    return (text[:n] + "…") if len(text) > n else text


def load_latest(json_dir: str):
    """读取最新的 creator_contents_*.json 与 creator_creators_*.json。"""
    contents_file = sorted(glob.glob(os.path.join(json_dir, "creator_contents_*.json")))[-1]
    creators_file = sorted(glob.glob(os.path.join(json_dir, "creator_creators_*.json")))[-1]
    with open(contents_file, encoding="utf-8") as f:
        raw = json.load(f)
    with open(creators_file, encoding="utf-8") as f:
        creator = json.load(f)[0]
    return contents_file, raw, creator


def dedupe(raw):
    """按 content_id 去重，保留 content_text 较丰富的一条。"""
    best = {}
    for c in raw:
        cid = c["content_id"]
        cur = best.get(cid)
        if cur is None or len(c.get("content_text") or "") > len(cur.get("content_text") or ""):
            best[cid] = c
    return list(best.values())


def fmt_date(ts) -> str:
    return time.strftime("%Y-%m-%d", time.localtime(ts)) if ts else "?"


def fmt_dt(ts) -> str:
    return time.strftime("%Y-%m-%d %H:%M", time.localtime(ts)) if ts else "?"


def build_collection(items, creator, contents_file, out_path, now_str):
    items_sorted = sorted(items, key=lambda x: x.get("created_time", 0), reverse=True)
    articles = [c for c in items_sorted if c["content_type"] == "article"]
    answers = [c for c in items_sorted if c["content_type"] == "answer"]

    lines = []
    lines.append("# 静水2008 · 知乎内容合集\n")
    lines.append("> 职业投资人，不带人不建群。\n")
    lines.append("**创作者信息**\n")
    link = creator.get('user_link')
    lines.append(f"- 昵称：{creator.get('user_nickname','静水2008')}　|　主页：[{link}]({link})")
    lines.append(f"- 粉丝：{creator.get('fans')}　|　获赞：{creator.get('get_voteup_count') or creator.get('voteup_count') or '—'}")
    lines.append(f"- 回答：{creator.get('anwser_count')}　|　文章：{creator.get('article_count')}　|　IP：{creator.get('ip_location','—')}")
    lines.append(f"- 更新时间：{now_str}　|　收录：回答 {len(answers)} 条 + 文章 {len(articles)} 篇")
    lines.append(f"- 数据来源：MediaCrawler（{os.path.basename(contents_file)}）　|　仅供学习研究，非投资建议\n")
    lines.append("---\n")
    # 目录
    lines.append("## 📑 目录（按时间排序，最新在前）\n")
    lines.append("| # | 类型 | 标题 / 摘要 | 时间 | 👍赞 | 原文 |")
    lines.append("|---|---|---|---|---|---|")
    for i, c in enumerate(items_sorted, 1):
        title = (c.get("title") if c["content_type"] == "article" else "") or excerpt(c.get("desc") or c.get("content_text"), EXCERPT_LEN_COLLECTION)
        kind = "文章" if c["content_type"] == "article" else "回答"
        url = c.get('content_url')
        lines.append(f"| {i} | {kind} | {title} | {fmt_date(c.get('created_time'))} | {c.get('voteup_count',0)} | [🔗]({url}) |")
    lines.append("\n---\n")
    # 专栏文章
    lines.append(f"## ✍️ 专栏文章（{len(articles)} 篇）\n")
    for c in articles:
        title = c.get("title") or excerpt(c.get("content_text"), EXCERPT_LEN_COLLECTION)
        lines.append(f"### {title}\n")
        url = c.get('content_url')
        lines.append(f"> 👍 {c.get('voteup_count',0)}　·　💬 {c.get('comment_count',0)}　·　🕐 {fmt_date(c.get('created_time'))}　·　[🔗 原文]({url})\n")
        lines.append((c.get("content_text") or "").strip() + "\n")
        lines.append("---\n")
    # 回答
    lines.append(f"## 💬 回答（{len(answers)} 条，最新在前）\n")
    for i, c in enumerate(answers, 1):
        head = excerpt(c.get("desc") or c.get("content_text"), EXCERPT_LEN_COLLECTION)
        lines.append(f"### {i}. {head}\n")
        url = c.get('content_url')
        lines.append(f"> 👍 {c.get('voteup_count',0)}　·　💬 {c.get('comment_count',0)}　·　🕐 {fmt_date(c.get('created_time'))}　·　[🔗 原文]({url})\n")
        lines.append((c.get("content_text") or "").strip() + "\n")
        lines.append("---\n")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines).rstrip() + "\n")
    return len(answers), len(articles)


def build_index(items, creator, contents_file, out_path, now_str):
    items_sorted = sorted(items, key=lambda x: x.get("voteup_count", 0), reverse=True)
    lines = []
    lines.append("# 静水2008 · 原文索引\n")
    lines.append(f"> {len(items_sorted)} 条回答/文章的元数据目录（按点赞排序），用于按需回溯原文。完整正文见 `…/MediaCrawler/data/zhihu/markdown/静水2008-知乎合集.md`（更新于 {now_str}）。\n")
    lines.append("| # | 类型 | 摘要 | 👍赞 | 💬评论 | 时间 | 原文 |")
    lines.append("|---|---|---|---|---|---|---|")
    for i, c in enumerate(items_sorted, 1):
        kind = "文章" if c["content_type"] == "article" else "回答"
        summ = excerpt(c.get("desc") or c.get("content_text"), EXCERPT_LEN_INDEX)
        url = c.get('content_url')
        lines.append(f"| {i} | {kind} | {summ} | {c.get('voteup_count',0)} | {c.get('comment_count',0)} | {fmt_date(c.get('created_time'))} | [🔗]({url}) |")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    return len(items_sorted)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json-dir", default=DEFAULT_JSON_DIR)
    ap.add_argument("--out-collection", default=DEFAULT_OUT_COLLECTION)
    ap.add_argument("--out-index", default=DEFAULT_OUT_INDEX)
    args = ap.parse_args()

    contents_file, raw, creator = load_latest(args.json_dir)
    items = dedupe(raw)
    now_str = fmt_dt(max(c.get("last_modify_ts", 0) or 0 for c in items) / 1000) if items else time.strftime("%Y-%m-%d %H:%M")

    n_ans, n_art = build_collection(items, creator, contents_file, args.out_collection, now_str)
    n_total = build_index(items, creator, contents_file, args.out_index, now_str)
    print(f"读取: {contents_file}")
    print(f"去重后: 回答 {n_ans} + 文章 {n_art} = {n_total} 条")
    print(f"写出合集: {args.out_collection}")
    print(f"写出索引: {args.out_index}")


if __name__ == "__main__":
    main()
