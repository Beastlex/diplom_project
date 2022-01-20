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
Убедиться в работоспособности можно по адресу http://<<Имя хоста>>

## Deploy в облако

Перейти в папку terraform и выполнить шаги, описанные в Terraform/README.md

В данном каталоге убедить, что получены credentials для Kubernetes
с помощью
```
az aks get-credentials --resource-group rg-alzver-proj  --name aks-alzver-proj
```
и убедить в работоспособности кластреа:
```
kubectl cluster-info
```
запустить манифесты Kubernetes
```
kubectl apply -f ./k8s/*
```

## Дополнитеьная презентация CI/CD в Azure DevOps
