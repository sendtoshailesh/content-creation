# Idea Queue — Cloud databases

> **Candidate source material** clustered from your Apple Notes + Chrome bookmarks + Chrome
> reading list (229 items matched this topic). These are raw inputs, not yet scored.
> Run `@feed-curator` (or `@reading-list-curator`) in this workspace to synthesize and
> rank them into content ideas, then `@content-pipeline` / `/topic-pipeline cloud-databases` to write.

Last seeded: 2026-06-11 by `scripts/pipeline/scaffold_topics.py`
(employer-internal and personal links excluded).

---

## Candidate source material

### From Apple Notes
- donnemartin/system-design-primer: Learn how to design large-scale…
- Database aws vs azure
- Introducing Amazon Aurora powers for Kiro / AWS Database Blog
- MongoDB Index Intersection (and PostgreSQL Bitmap-and) - DEV Community
- In S3 simplicity is table stakes

### From Chrome bookmarks
- [Link GitHub commits, PRs, branches, and issues to work items - Azure Boards / Microsoft Learn](https://learn.microsoft.com/en-us/azure/devops/boards/github/link-to-from-github?view=azure-devops)
- [Performance Insights metrics for DB instances - AWS Prescriptive Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-rds-monitoring-alerting/db-instance-performance-insights.html)
- [SQL statistics for Aurora PostgreSQL - Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.PostgreSQL.html)
- [Parameters tuning for Amazon Aurora/RDS/EC2 for PostgreSQL](https://apg-library.amazonaws.com/content/b12fc9fb-3421-4351-b038-e5194ed599d9#best-practices-for-tuning-memory-parameters)
- [Improve app performance through pipelining queries to Amazon RDS for PostgreSQL and Amazon Aurora Po](https://aws.amazon.com/blogs/database/improve-app-performance-through-pipelining-queries-to-amazon-rds-for-postgresql-and-amazon-aurora-postgresql/)
- [Leverage pgvector and Amazon Aurora PostgreSQL for Natural Language Processing, Chatbots and Sentime](https://aws.amazon.com/blogs/database/leverage-pgvector-and-amazon-aurora-postgresql-for-natural-language-processing-chatbots-and-sentiment-analysis/)
- [Optimize generative AI applications with pgvector indexing: A deep dive into IVFFlat and HNSW techni](https://aws.amazon.com/blogs/database/optimize-generative-ai-applications-with-pgvector-indexing-a-deep-dive-into-ivfflat-and-hnsw-techniques/)
- [Monitor query plans for Amazon Aurora PostgreSQL / AWS Database Blog](https://aws.amazon.com/blogs/database/monitor-query-plans-for-amazon-aurora-postgresql/)
- [How PostgreSQL processes queries and how to analyze them / AWS Database Blog](https://aws.amazon.com/blogs/database/how-postgresql-processes-queries-and-how-to-analyze-them/)
- [The role of vector datastores in generative AI applications / AWS Database Blog](https://aws.amazon.com/blogs/database/the-role-of-vector-datastores-in-generative-ai-applications/)
- [Understanding autovacuum in Amazon RDS for PostgreSQL environments / AWS Database Blog](https://aws.amazon.com/blogs/database/understanding-autovacuum-in-amazon-rds-for-postgresql-environments/)
- [Working with the PostgreSQL autovacuum on Amazon RDS for PostgreSQL - Amazon Relational Database Ser](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum.html)
- [Troubleshoot Amazon Aurora PostgreSQL Performance by Use Case](https://catalog.us-east-1.prod.workshops.aws/workshops/af784ecc-7ceb-4b86-8c7c-e03cbdbe4e0d/en-US)
- [Generative AI use cases with Aurora PostgreSQL](https://catalog.workshops.aws/pgvector/en-US)
- [Managing object dependencies in PostgreSQL – Overview and helpful inspection queries (Part 1) / AWS ](https://aws.amazon.com/blogs/database/managing-object-dependencies-in-postgresql-overview-and-helpful-inspection-queries-part-1/)
- [Managing object dependencies in PostgreSQL: Removing dependent objects (Part2) / AWS Database Blog](https://aws.amazon.com/blogs/database/managing-object-dependencies-in-postgresql-removing-dependent-objects-part2/)
- [Automate on-premises or Amazon EC2 SQL Server to Amazon RDS for SQL Server migration using custom lo](https://aws.amazon.com/blogs/database/automate-on-premises-or-amazon-ec2-sql-server-to-amazon-rds-for-sql-server-migration-using-custom-log-shipping/)
- [Reduce database patching downtime in Amazon RDS Custom for Oracle using Oracle Data Guard Standby-Fi](https://aws.amazon.com/blogs/database/reduce-database-patching-downtime-in-amazon-rds-custom-for-oracle-using-oracle-data-guard-standby-first-patch-apply/)
- [Achieve minimal downtime for major and minor version upgrades of Amazon RDS for Oracle using Oracle ](https://aws.amazon.com/blogs/database/achieve-minimal-downtime-for-major-and-minor-version-upgrades-of-amazon-rds-for-oracle-using-oracle-goldengate/)
- [Build high availability for Amazon RDS Custom for Oracle using read replicas / AWS Database Blog](https://aws.amazon.com/blogs/database/build-high-availability-for-amazon-rds-custom-for-oracle-using-read-replicas/)
- [The Business Value of Adopting Amazon Web Services Managed Databases.pdf](https://pages.awscloud.com/rs/112-TZM-766/images/The%20Business%20Value%20of%20Adopting%20Amazon%20Web%20Services%20Managed%20Databases.pdf)
- [Managed Oracle Data Guard Switchover with Amazon RDS for Oracle / AWS Database Blog](https://aws.amazon.com/blogs/database/managed-oracle-data-guard-switchover-with-amazon-rds-for-oracle/)
- [Rethink Oracle Standard Edition Two on Amazon RDS for Oracle / AWS Database Blog](https://aws.amazon.com/blogs/database/rethink-oracle-standard-edition-two-on-amazon-rds-for-oracle/)
- [Community / Architecting for Zero Data Loss Disaster Recovery using Amazon RDS Solutions](https://community.aws/posts/zero-dataloss-dr-using-rds)
- [Choosing the right database for your RTO and RPO requirements - AWS Prescriptive Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-database-disaster-recovery/choosing-database.html)
- [RDSTools](https://rdstools.d1m9acb3dnc55n.amplifyapp.com/)
- [How to plan for a successful database modernization / AWS Database Blog](https://aws.amazon.com/blogs/database/how-to-plan-for-a-successful-database-modernization/)
- [Validate database objects post-migration from Microsoft SQL Server to Amazon RDS for PostgreSQL and ](https://aws.amazon.com/blogs/database/validate-database-objects-post-migration-from-microsoft-sql-server-to-amazon-rds-for-postgresql-and-amazon-aurora-postgresql/)
- [Overview - SQL Server to Aurora PostgreSQL Migration Playbook](https://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-postgresql-migration-playbook/chap-sql-server-aurora-pg.html)
- [Migrate SQL Server to Amazon Aurora PostgreSQL using best practices and lessons learned from the fie](https://aws.amazon.com/blogs/database/migrate-sql-server-to-amazon-aurora-postgresql-using-best-practices-and-lessons-learned-from-the-field/)
- [Migration tips for developers converting Oracle and SQL Server code to PostgreSQL / AWS Database Blo](https://aws.amazon.com/blogs/database/code-conversion-challenges-while-migrating-from-oracle-or-microsoft-sql-server-to-postgresql/)
- [Use the tds_fdw extension to migrate data from SQL Server to PostgreSQL / AWS Database Blog](https://aws.amazon.com/blogs/database/use-the-tds_fdw-extension-to-migrate-data-from-sql-server-to-postgresql/)
- [Amazon RDS Instance Comparison](https://instances.vantage.sh/rds/)
- [AWS Database Migration Service / AWS Database Blog](https://aws.amazon.com/blogs/database/category/migration/aws-database-migration-service-migration/)
- [AWS Database Migration Service Best Practices](https://d0.awsstatic.com/whitepapers/RDS/AWS_Database_Migration_Service_Best_Practices.pdf)
- [Convert database schemas and application SQL using the AWS Schema Conversion Tool CLI / AWS Database](https://aws.amazon.com/blogs/database/convert-database-schemas-and-application-sql-using-the-aws-schema-conversion-tool-cli/)
- [Schema and code validator for Oracle to Amazon RDS for PostgreSQL or Amazon Aurora PostgreSQL migrat](https://aws.amazon.com/blogs/database/schema-and-code-validator-for-oracle-to-amazon-rds-for-postgresql-or-amazon-aurora-postgresql-migration/)
- [Use virtual partitioning in the AWS Schema Conversion Tool / AWS Database Blog](https://aws.amazon.com/blogs/database/use-virtual-partitioning-in-the-aws-schema-conversion-tool/)
- [AWS Schema Conversion Tool blog series: Introducing new features in build 617 / AWS Database Blog](https://aws.amazon.com/blogs/database/aws-schema-conversion-tool-blog-series-introducing-new-features-in-build-617/)
- [AWS Schema Conversion Tool introduces new features in build 616 / AWS Database Blog](https://aws.amazon.com/blogs/database/aws-schema-conversion-tool-blog-series-introducing-new-features-in-build-616/)

### From Chrome reading list
- [introducing the aurora storage engine](https://aws.amazon.com/blogs/database/introducing-the-aurora-storage-engine/)
- [using rds proxy with](https://aws.amazon.com/blogs/database/using-rds-proxy-with-)
- [postgres](https://github.com/awslabs/rds-support-tools/tree/main/postgres)
- [multi agentic rag with hugging face code](https://towardsdatascience.com/multi-agentic-rag-with-hugging-face-code-)
- [beyond query optimization aurora postgres connection pooling with sqlalchemy rdsproxy 200db7f562d7](https://eng.lyft.com/beyond-query-optimization-aurora-postgres-connection-pooling-with-sqlalchemy-rdsproxy-200db7f562d7)
- [how to measure ai value](https://towardsdatascience.com/how-to-measure-ai-value/?utm_campaign=tds%20variable&utm_medium=email&_hsenc=p2ANqtz-_3sTNzmkYyfHnZMpKA2160_s4rdIt7Q5dAVvXn0z2c0xTgMBk3Yy4ZSi4Bmiuyiy0J0-j6UiiSMUx60VlpA65S_Er2oQ&_hsmi=410502984&)

---

## Queued Ideas

<!-- Synthesized, scored ideas are appended here by @feed-curator. -->
