

[![Deployment Pipeline](https://github.com/GastonFenske/article-ms-azure/actions/workflows/pipeline.yml/badge.svg)](https://github.com/GastonFenske/article-ms-azure/actions/workflows/pipeline.yml)
<!-- [![Stable Version](https://img.shields.io/github/v/tag/anothrNick/github-tag-action)](https://img.shields.io/github/v/tag/anothrNick/github-tag-action)
[![Latest Release](https://img.shields.io/github/v/release/anothrNick/github-tag-action?color=%233D9970)](https://img.shields.io/github/v/release/anothrNick/github-tag-action?color=%233D9970) -->


# stocklister.azurecr.io/article-ms-azure:v3

docker build . -t ${{ secrets.ACR_NAME }}/${{ env.REPO_NAME }}:${{ steps.tag.outputs.tag }}
docker push ${{ secrets.ACR_NAME }}/${{ env.REPO_NAME }}:${{ steps.tag.outputs.tag }}