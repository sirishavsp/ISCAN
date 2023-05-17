variable "access_key" {
  description = "The access_key"
  type = string
}

resource "aws_instance" "bgrwyesqdl" {
  access_key = var.access_key
}

output "access_key" {
  value = aws_instance.bgrwyesqdl.access_key
}

module "secure_module" {
  source = "./modules/cvpyzdpncj"
  access_key = var.access_key
}
