import os


def remorcao_container():
    print("Removendo todos os containers.")
    os.system("docker compose down")
    containers = os.popen("docker ps -aq").read().split("\n")
    containers.remove('')
    if len(containers) > 0:
        print("Foram encontrados os containers {}".format(containers))
        for container in containers:
            print("Parando container {}".format(container))
            #Parar container
            os.system("docker container stop {}".format(container))   
        #Excluir containers que existem mas estão parados
        os.system("docker container prune -f")
        

if __name__ == "__main__":
    print("Remorção containers iniciada!")
    remorcao_container()