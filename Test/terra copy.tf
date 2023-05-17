resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"

  # This line uses HTTP (unencrypted) instead of HTTPS
  user_data     = "http://example.com/myscript.sh"

  # This script file has insecure file permissions
  provisioner "file" {
    source      = "scripts/myscript.sh"
    destination = "/tmp/myscript.sh"
    connection {
      type        = "ssh"
      user        = "ubuntu"
      private_key = file("mykey.pem")
    }
  }
}
resource "aws_db_instance" "example" {
  allocated_storage    = 10
  engine               = "mysql"
  engine_version       = "5.6.17"
  instance_class       = "db.t2.micro"
  name                 = "mydb"
  username             = "admin"
  password             = "password123" # This password is weak and easily guessable
}
resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  key_name      = "example-key"
  security_groups = ["${aws_security_group.example.id}"]

  connection {
    type        = "ssh"
    user        = "ec2-user"
    password    = "plaintextpassword"
    private_key = file("example-key.pem")
    timeout     = "1m"
    port        = 22
    host        = self.public_ip
  }

  provisioner "remote-exec" {
    inline = [
      "echo 'Hello, World!'",
      "md5sum /var/log/messages",
      "openssl rc4 -e -in /var/log/messages -out /var/log/messages.enc",
      "ftp example.com",
      "telnet example.com 23",
      "rlogin example.com",
      "rsh example.com",
      "tftp example.com",
      "sendmail -t < /tmp/message.txt",
      "smtp example.com"
    ]
  }
}

