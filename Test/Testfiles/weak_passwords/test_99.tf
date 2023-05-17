variable "ssh_key" {
  description = "The ssh_key"
  type = string
}

resource "aws_vpc" "oiuexglxpp" {
  ssh_key = var.ssh_key
}

output "ssh_key" {
  value = aws_vpc.oiuexglxpp.ssh_key
}

module "secure_module" {
  source = "./modules/mlkclulqtd"
  ssh_key = var.ssh_key
}
