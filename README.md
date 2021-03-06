# Итоговая работа Зверева Александра

Приложение представляет из себя сервис хранения статистики
заболеваемости COVID-19 c ресурса ...

Используется нативная БД от Azure для хранения результатов.
Само приложение реализовано в виде нескольких служб и контейнеров
для Kubernetes. В качестве стэка выбраны Flask и Nginx

## Локальное тестирование

Для локального тестирования используется docker-compose.
Используется дополнительные контейнеры, собранные на базе
traefik и postgres.
Для запуска локальной версии:
```
docker-compose up --build
```
Убедиться в работоспособности можно по адресу http://<<Имя хоста>>:8000

## Deploy в облако

Создать диреторию для хранения ssh ключей для нод кластера и файла с
паролем для БД.

```console
mkdir -p $HOME/.ssh/aks-alzver-proj/
```
в диретории создать файл dbsec.txt, содержащий пароль для БД

Создать из файла secret для Kubernetes
```console
kubectl create secret generic proj-secret \ 
  --from-file=$HOME/.ssh/aks-alzver-proj/dbsec.txt \
  --dry-run=client --output=yaml > k8s/01-secret.yaml
```

Перейти в папку terraform и выполнить шаги, описанные в Terraform/README.md


Залогиниться в реестр контейнеров
```
az acr login --name acr2022alzver
```

Перейти в каталог backend, собрать и запушить образ
```
docker build -t acr2022alzver.azurecr.io/backend:v1 .
docker push acr2022alzver.azurecr.io/backend:v1
```

Перейти в каталог frontend, собрать и запушить
```
docker build -t acr2022alzver.azurecr.io/frontend:v1 .
docker push acr2022alzver.azurecr.io/frontend:v1
```

В данном каталоге убедиться, что получены credentials для Kubernetes
с помощью
```
az aks get-credentials --resource-group rg-alzver-proj  --name aks-alzver-proj
```
и убедить в работоспособности кластреа:
```
kubectl cluster-info
```
Чтобы просто развернуть кластре - запустить манифесты Kubernetes
```
kubectl apply -f k8s/
```

С помощью helm есть возможность развернуть две среды (test и production)
Создать namespace
```console
kubectl create namespace test
kubectl create namespace production
```

Далее запустить чарты
```console
cd chart
helm install aks-alzver-test aks-alzver -n test -f values-test.yaml
helm install aks-alzver-prod aks-alzver -n production -f values-prod.yaml
```

Мониторинг
Добавить репозиторий 
```
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
```

 Установить чарт
 ```
 helm install prometheus \                                                 
  prometheus-community/kube-prometheus-stack \
  --namespace monitoring \
  --create-namespace
 ```
 
 По умолчанию Grafana не имеет доступа извне. Можно пробросить порт
 ```
 kubectl port-forward --namespace monitoring svc/prometheus-grafana 8080:80
 ```
 
## Дополнитеьная презентация CI/CD в Azure DevOps
