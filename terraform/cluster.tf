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

  identity {
    type = "SystemAssigned"
  }

  addon_profile {
    azure_policy { enabled = true }
    oms_agent {
      enabled                    = true
      log_analytics_workspace_id = azurerm_log_analytics_workspace.insights-alzver-proj.id
    }
  }

  tags = {
    owner = var.owner
  }
}
