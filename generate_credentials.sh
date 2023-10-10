
GROUP_NAME=umGroupResource
APP_NAME=universidad
SUSCRIPTION_ID=9682b5b1-86a1-4971-982c-b5ae60c23814

# echo $ACR_REGISTRY_ID

az ad sp create-for-rbac --name $APP_NAME --role contributor \
                        --scopes /subscriptions/$SUSCRIPTION_ID/resourceGroups/$GROUP_NAME \
                        --sdk-auth