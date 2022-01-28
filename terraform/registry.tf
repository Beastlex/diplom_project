resource "azurerm_container_registry" "acr-alzver-proj" {
  name                   = "acr2022alzver"
  resource_group_name    = azurerm_resource_group.rg-alzver-proj.name
  location               = var.location
  sku                    = "Standard"
  admin_enabled          = true
  anonymous_pull_enabled = true

  tags = {
    owner = var.owner
  }
}

/*
resource "azurerm_role_assignment" "aks-to-acr" {
  scope                = azurerm_container_registry.acr-alzver-proj.id
  role_definition_name = "AcrPull"
  principal_id         = azurerm_kubernetes_cluster.aks-alzver-proj.kubelet_identity[0].object_id
}
*/
