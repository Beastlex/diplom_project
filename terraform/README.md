# Создать директорию для хранения ключей
mkdir $HOME/.ssh/aks-alzver-proj

# Сгенерировать ключ
ssh-keygen \
    -m PEM \
    -t rsa \
    -b 4096 \
    -C "azureuser@aks-alzver-proj" \
    -f ~/.ssh/aks-alzver-proj/aks-ssh-key
