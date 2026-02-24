"""singularity pull docker://rocm/pytorch:rocm7.0.2_ubuntu24.04_py3.12_pytorch_release_2.6.0
"""
##Setup enviroments variables
git config --global http.proxy $http_proxy
git config --global https.proxy $https_proxy
git config --global http.proxyAuthMethod 'basic'

$http_proxy
http://svc_proxy_nonrte_netgrp:jLNgeTuuCdbu9h9kesPaA4iEDrzHvXtR@172.22.13.140:3128git config --global http.proxy "$http_proxy"
git config --global https.proxy "$https_proxy"
git config --global http.proxyAuthMethod 'basic'

singularity shell -B ~/:/workspace 
export HF_HOME=/vast/users/hisham.cholakkal/documents/cachepath/hf
export MIOPEN_USER_DB_PATH="/vast/users/hisham.cholakkal/tmp_dir/miopen_node8"
export MIOPEN_CUSTOM_CACHE_DIR=${MIOPEN_USER_DB_PATH}
rm -rf ${MIOPEN_USER_DB_PATH}
mkdir -p ${MIOPEN_USER_DB_PATH}

cd /workspace/documents/rewardit/DanceGRPO/