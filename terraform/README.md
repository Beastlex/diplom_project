# Создать директорию для хранения ключей
```
mkdir $HOME/.ssh/aks-alzver-proj
```

# Сгенерировать ключ
```
ssh-keygen \
    -m PEM \
    -t rsa \
    -b 4096 \
    -C "azureuser@aks-alzver-proj" \
    -f ~/.ssh/aks-alzver-proj/aks-ssh-key
```

# Выполнить вход в учетную запись Azure
```
az login
```

# Развернуть инфраструктуру Terraform, последовательно выполняя
```
terraform init
terraform plan
terraform apply
```

# Получить учетные данные для kubectl 
```
az aks get-credentials --resource-group rg-alzver-proj  --name aks-alzver-proj
```

# Проверить информацию о кластере 
```
kubectl cluster-info
```

# Получить информацию о нодах
```
kubectl get nodes
```
