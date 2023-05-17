variable "access_key" {
  description = "The access_key"
  type = string
}

resource "aws_security_group" "obmmufrlkc" {
  access_key = var.access_key
}

output "access_key" {
  value = aws_security_group.obmmufrlkc.access_key
}

module "secure_module" {
  source = "./modules/xtaerhhppx"
  access_key = var.access_key
}
