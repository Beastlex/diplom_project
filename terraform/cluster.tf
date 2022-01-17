resource "azurerm_kubernetes_cluster" "aks-alzver-proj" {
  name                = "aks-${var.postfix}"
  location            = var.location
  resource_group_name = azurerm_resource_group.rg-alzver-proj.name
  dns_prefix          = "aks-${var.postfix}"

  default_node_pool {
    name                 = "mainpool"
    vm_size              = "Standard_D2_v2"
    enable_auto_scailing = true
    min_count            = 1
    max_count            = 2
    vnet_subnet_id       = azurerm_subnet.subnet-aks.id
    tags = {
      owner = var.owner
    }
  }

  tags = {
    owner = var.owner
  }
}
