# Terraform module to setup postgresql instance at Azure cloud
resource "azurerm_resource_group" "default" {
  name     = join(var.env_name, "-resources")
  location = var.location
}

resource "azurerm_postgresql_server" "default" {
  name                = join(var.env_name, "-psqlserver")
  location            = azurerm_resource_group.default.location
  resource_group_name = azurerm_resource_group.default.name

  administrator_login          =  var.admin_username
  administrator_login_password = var.admin_password

  sku_name   = "GP_Gen5_4"
  version    = "11"
  storage_mb = 640000

  backup_retention_days        = 7
  geo_redundant_backup_enabled = true
  auto_grow_enabled            = true

  public_network_access_enabled    = false
  ssl_enforcement_enabled          = true
  ssl_minimal_tls_version_enforced = "TLS1_2"
}