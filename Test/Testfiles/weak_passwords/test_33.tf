variable "access_key" {
  description = "The access_key"
  type = string
}

resource "aws_instance" "mymbqigfzo" {
  access_key = var.access_key
}

output "access_key" {
  value = aws_instance.mymbqigfzo.access_key
}

module "secure_module" {
  source = "./modules/fwzzukurcf"
  access_key = var.access_key
}
