# jazzhr_tap

## Quick start

1. Virtual environment
- Create a virtual environment

    ``` shell script
    python3 -m venv environment_name
    ````

- Active virtual environment

    ``` shell script
    source environment_name/bin/activate
    ````


2. Install
- Clone this project

    ``` shell script
    git clone https://github.com/oscarrussi/jazzhr_tap.git
    ````

- In the jazzhr_tap/jazzhr_reources/schemas folder, create keys.json file and add you key:

    ```javascript
    {"jazzhr_key": "your_key"}
    ```

- In the jazzhr_tap folder, install the package

    ``` shell script
    pip install .
    ````

3. Create config file

- In jazzhr_tap/jazzhr_reources folder, create config.json file and your stitch credentials (Token and client_id):

    ```javascript
    {
    "client_id" : your_client_id,
    "token" : "your_token",
    "small_batch_url": "https://api.stitchdata.com/v2/import/batch",
    "big_batch_url": "https://api.stitchdata.com/v2/import/batch",
    "batch_size_preferences": {}
    }
    ```

4. Run tap

- In jazzhr_resources folder, run the tap as a package using the next shell command:

    ``` shell script
    jazzhr_tap | target-stitch --config config.json
    ````
- Or as an alternative, you can running it as a module, in jazzhr_resources folder:

    ``` shell script
    python3 -m jazzhr_resources | target-stitch --config config.json
    ````

##  Entity relation diagram


![screenshot](er_diagram.png)