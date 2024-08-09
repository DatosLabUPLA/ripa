
REM Process works files
for /R "openalex-snapshot\data\works" %%f in (*.gz) do (
    bq load --source_format=CSV -F "\t" --schema "work:string" --project_id ripa-1022 openalex.works %%f
)

REM Process authors files
for /R "openalex-snapshot\data\authors" %%f in (*.gz) do (
    bq load --source_format=CSV -F "\t" --schema "author:string" --project_id ripa-1022 openalex.authors %%f
)

REM Process sources files
for /R "openalex-snapshot\data\sources" %%f in (*.gz) do (
    bq load --source_format=CSV -F "\t" --schema "source:string" --project_id ripa-1022 openalex.sources %%f
)

REM Process institutions files
for /R "openalex-snapshot\data\institutions" %%f in (*.gz) do (
    bq load --source_format=CSV -F "\t" --schema "institution:string" --project_id ripa-1022 openalex.institutions %%f
)

REM Process concepts files
for /R "openalex-snapshot\data\concepts" %%f in (*.gz) do (
    bq load --source_format=CSV -F "\t" --schema "concept:string" --project_id ripa-1022 openalex.concepts %%f
)

REM Process publishers files
for /R "openalex-snapshot\data\publishers" %%f in (*.gz) do (
    bq load --source_format=CSV -F "\t" --schema "publisher:string" --project_id ripa-1022 openalex.publishers %%f
)

echo Finished processing all files.
