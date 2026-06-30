---
title: Creative Brief - PostgreSQL 18 Skip Scan
description: Creative brief for a content pipeline run on PostgreSQL 18's B-tree skip scan and the redundant indexes it lets you delete
author: Shailesh Mishra
ms.date: 2026-06-29
ms.topic: concept
keywords:
  - postgresql 18
  - skip scan
  - b-tree index
  - redundant indexes
  - write amplification
  - database cost optimization
estimated_reading_time: 7
---

## Creative Brief

> Status: `approved` · Run topic: PostgreSQL 18 Skip Scan — the redundant index you no longer have to build
> Created: 2026-06-29 · Idea source: `content/postgresql-idea-log.md` [1] · Branch: dedicated (main untouched)

## 1. Overview

PostgreSQL 18 (GA 25 Sep 2025) shipped B-tree **skip scan**. Before it, a multicolumn index on `(a, b)` was useless to a query that filtered only on `b` — the planner needed the leading column. So everyone learned the same reflex: add a second, single-column index on `b`. That extra index is paid on every write (write amplification) and in storage/backups, forever. Skip scan lets the planner "skip" through distinct leading values and reuse `(a, b)` for `b`-only queries — so the redundant index can finally be dropped. One feature, four payoffs: faster reads, cheaper writes, less disk, and a clean upgrade story.

## 2. Objectives
- **Primary JTBD:** convince a PostgreSQL practitioner that upgrading to 18 lets them delete redundant single-column indexes, and show them how to find and verify the candidates.
- **Secondary:** make the perf + cost link explicit (each index is a tax on every write); keep it honest about when skip scan does NOT help.

## 3. Audience
- Primary: app/backend engineers + DBAs running Postgres in prod past the novice stage.
- Secondary: tech leads/managers who care about the cloud DB bill and write throughput.

## 4. Key message
PostgreSQL 18's skip scan deletes the redundant index you only created to satisfy the planner — so you read faster, write faster, and store less, with no app changes.

## 5. Tone & style
First-person practitioner, data-anchored, EXPLAIN snippets, ~2,200 words. No hype.

## 6. Deliverables
- Blog (primary), 4 visuals, LinkedIn post (plain + Unicode). Out of scope: X, Reddit, YouTube, deck.

## 7. Visuals
Design tokens; before/after index ladder, write-amplification cost, EXPLAIN flip, decision checklist.

## 8. CTA
Run the redundant-index query on a replica, drop one duplicate after upgrading to 18, watch writes speed up.

## 9. Guardrails
Cite postgresql.org news + 18 docs. Be honest: skip scan wins when leading column has low cardinality; high-cardinality leads gain little.

## 10. One-sentence thesis
The cheapest performance win in PostgreSQL 18 is the index you get to delete.
