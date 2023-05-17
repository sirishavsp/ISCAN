variable "access_key" {
  description = "The access_key"
  type = string
}

resource "aws_instance" "efqrrvrumv" {
  access_key = var.access_key
}

output "access_key" {
  value = aws_instance.efqrrvrumv.access_key
}

module "secure_module" {
  source = "./modules/vleyzvtled"
  access_key = var.access_key
}
