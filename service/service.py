from dao.dao import TesteDao


class ServiceTest:
    def selectClientes():
        conex = TesteDao.conectar()
        results = TesteDao.selectClientes(conex[0])
        return results

    def selectCliente(cpf):
        conex = TesteDao.conectar()
        results = TesteDao.selectCliente(conex[0], cpf)
        return results

    def criarCliente(userDetails):
        conex = TesteDao.conectar()
        results = TesteDao.criarCliente(conex[0], conex[1], userDetails)
        return results

    def updateCliente(userDetails):
        conex = TesteDao.conectar()
        results = TesteDao.updateCliente(conex[0], conex[1], userDetails)
        return results

    def deleteCliente(cpf):
        conex = TesteDao.conectar()
        results = TesteDao.deleteCliente(conex[0], conex[1], cpf)
        return results
