#! /bin/sh
# sh app-shell-script.sh
nohup python3 ../app.py run --config-yaml config_files/.test_env_config_fact_store_es.yaml > nohup.out 2>&1 &