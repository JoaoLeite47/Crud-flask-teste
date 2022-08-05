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

    def selectCategorias():
        conex = TesteDao.conectar()
        results = TesteDao.selectCategorias(conex[0])
        return results
    
    def selectCategoria(cod_categ):
        conex = TesteDao.conectar()
        results = TesteDao.selectCategoria(conex[0], cod_categ)
        return results

    def criarCategoria(userDetails):
        conex = TesteDao.conectar()
        results = TesteDao.criarCategoria(conex[0], conex[1], userDetails)
        return results

    def updateCategoria(userDetails,):
        conex = TesteDao.conectar()
        results = TesteDao.updateCategoria(conex[0], conex[1], userDetails,)
        return results

    def deleteCategoria(cod_categ):
        conex = TesteDao.conectar()
        results = TesteDao.deleteCategoria(conex[0], conex[1], cod_categ)
        return results
    
    def selectAlocacoes():
        conex = TesteDao.conectar()
        results = TesteDao.selectAlocacoes(conex[0])
        return results
    
    def selectAlocacao(cod_aloc):
        conex = TesteDao.conectar()
        results = TesteDao.selectAlocacao(conex[0], cod_aloc)
        return results

    def criarAlocacao(userDetails):
        conex = TesteDao.conectar()
        results = TesteDao.criarAlocacao(conex[0], conex[1], userDetails)
        return results

    def updateAlocacao(userDetails):
        conex = TesteDao.conectar()
        results = TesteDao.updateAlocacao(conex[0], conex[1], userDetails)
        return results

    def deleteAlocacao(cod_aloc):
        conex = TesteDao.conectar()
        results = TesteDao.deleteAlocacao(conex[0], conex[1], cod_aloc)
        return results
