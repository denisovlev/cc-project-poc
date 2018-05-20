aws_config = (JSON.parse(File.read("aws-config.json")))

Vagrant.configure("2") do |config|

    config.vm.box = "dummy"
    config.vm.box_url = "https://github.com/mitchellh/vagrant-aws/raw/master/dummy.box"

    aws_config['instances'].each do |instance|
        instance_key   = instance[0]
        instance_value = instance[1]

        config.vm.define instance_key do |config2|
	    ec2_tags = instance_value['tags']

            config2.vm.provider :aws do |ec2, override|
                ec2.access_key_id = ENV['AWS_ACCESS_KEY']
                ec2.secret_access_key = ENV['AWS_SECRET_KEY']
                ec2.keypair_name = ENV['AWS_EC2_KEY_NAME']
                ec2.region = aws_config['region']
                ec2.availability_zone = aws_config['region']+aws_config['availability_zone']
                ec2.subnet_id = aws_config['subnet_id']
                ec2.security_groups = aws_config['security_groups']
                ec2.ami = aws_config['ami_id']
                ec2.instance_type = aws_config['instance_type']
                ec2.private_ip_address = instance_value['private_ip_address']
                ec2.elastic_ip=instance_value['elastic_ip']
                ec2.tags = {
                    'Name' => ec2_tags['Name'],
                    'Role' => ec2_tags['Role']
		        }
		        override.ssh.username = aws_config['ssh_username']
                override.ssh.private_key_path = ENV['AWS_PRIVATE_KEY_PATH']

            end
        end
    end

    config.vm.provision "ansible" do |ansible|
        ansible.playbook = "Playbook.yml"
    end

end
