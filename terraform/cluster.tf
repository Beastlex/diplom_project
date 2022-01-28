resource "azurerm_kubernetes_cluster" "aks-alzver-proj" {
  name                = "aks-${var.postfix}"
  location            = var.location
  resource_group_name = azurerm_resource_group.rg-alzver-proj.name
  dns_prefix          = "aks-${var.postfix}"

  default_node_pool {
    name                = "systempool"
    vm_size             = "Standard_D2_v2"
    enable_auto_scaling = true
    min_count           = 1
    max_count           = 3
    vnet_subnet_id      = azurerm_subnet.subnet-aks.id
    tags = {
      owner = var.owner
    }
  }

  network_profile {
    network_plugin     = "azure"
    service_cidr       = "10.0.4.0/24"
    dns_service_ip     = "10.0.4.10"
    docker_bridge_cidr = "172.17.0.1/16"
    load_balancer_sku  = "Standard"
  }

  identity {
    type = "SystemAssigned"
  }

  linux_profile {
    admin_username = "worker"
    ssh_key {
      key_data = file(var.ssh-public-key)
    }
  }

  addon_profile {
    azure_policy { enabled = true }

    oms_agent {
      enabled                    = true
      log_analytics_workspace_id = azurerm_log_analytics_workspace.insights-alzver-proj.id
    }

    ingress_application_gateway {
      enabled   = true
      subnet_id = azurerm_subnet.subnet-gw.id
    }
  }

  tags = {
    owner = var.owner
  }
}
