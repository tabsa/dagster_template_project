# dagster_template_project
Repository to explore dagster templates and quick start guide.

I have followed the guides provided by dagster in the [documentation section](https://docs.dagster.io/).

## Build first dagster pipeline
I started by implementing the dagster [quick-start](https://docs.dagster.io/getting-started/quickstart) guide by adapting to this template project, so I have adopted the following structure:
```
└── dagster_template_project
   ├── src
   │   └── dagster_template_project
   │       ├── __init__.py
   │       ├── definitions.py
   │       └── defs
   │           └── __init__.py
   ├── data
   │   └── sample_data.csv
   ├── tests
   │   └── __init__.py
```
I also used the `sample_data.csv` part of the **quick-start** guide. As part of this quick-start guide, you have to create the `workspace.yaml` file so dagster knows **what code to load** when you run `dagster dev`.

For this guide, the `workspace` file content is 
```yaml
load_from:
  - python_file: src/dagster_template_project/definitions.py
```
Then you run the CLI command `dagster dev`.