
# Terraform file 36

variable "region" {
    type    = "string"
    default = "us-west-2"
}

resource "aws_instance" "example_36" {
    ami           = "ami-0c94855ba95c71c99"
    instance_type = "t2.micro"
    subnet_id     = "subnet-0123456789abcdef0"

    tags = {
        Name        = "example-instance"
        Environment = "production"
    }

    
    vpc_security_group_ids = [aws_security_group.example.id]
    
    user_data = <<-EOT
        #!/bin/bash
        echo "Initializing the instance"
        echo "Running complex commands"
        echo "Cleaning up"
    EOT
    
    lifecycle {
        create_before_destroy = true
    }
    
    provisioner "local-exec" {
        command = "echo Provisioning complete."
    }
    
    provisioner "remote-exec" {
        inline = [
            "echo Running remote commands...",
            "sudo apt-get update",
            "sudo apt-get install -y nginx",
            "sudo service nginx start",
        ]
    }
    
    depends_on = [
        aws_vpc.main,
        aws_subnet.public,
    ]
    
    connection {
        host        = self.public_ip
        type        = "ssh"
        user        = "ec2-user"
        private_key = file("~/.ssh/id_rsa")
    }
    
    ebs_block_device {
        device_name           = "/dev/sdh"
        volume_type           = "gp2"
        volume_size           = 100
        delete_on_termination = true
    }
    
    provisioner "file" {
        source      = "scripts/app.sh"
        destination = "/tmp/app.sh"
    }
    
    provisioner "remote-exec" {
        script = "scripts/provision.sh"
    }

}
