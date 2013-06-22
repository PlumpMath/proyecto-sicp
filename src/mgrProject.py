from sicp import db, app

class MgrProject():

    def guardar(self,project):
        """ 
        Guarda un registro project 
        @param project registro proyecto 
        """
        db.session.add(project)
        db.session.commit()
    
    
    def borrar(self,nombre):
        """ 
        Borra un registro project x name
        @param nombre nombre del proyecto que se desea borrar
        """
        from models import Proyecto
        project = Proyecto.query.filter(Proyecto.nombre == nombre).first_or_404()
        db.session.delete(project)
        db.session.commit()
    
    def modificar(self, nombre, nombreNew, descripcionNew, presupuestoNew):
        """
        Modificar un registro project x name
        @nombre nombre del registro proyecto que se desea modificar 
        @nombreNew nuevo nombre que se desea asignar al registro proyecto
        @descripcionNew nueva descripcion que se desea asingar al registro proyecto
        @presupuestoNew nuevo presupuesto que se desea asignar al registro proyecto
        """
        from models import Proyecto
        project = Proyecto.query.filter(Proyecto.nombre == nombre).first_or_404()
        project.nombre = nombreNew
        project.descripcion = descripcionNew
        project.presupuesto = presupuestoNew
        db.session.commit()
    
    def listar(self):
        """ listar proyectos """
        from models import Proyecto
        return Proyecto.query.all()
       
    def filtrar(self, nombre):
        """ 
        Filtrar proyecto por nombre 
        @nombre busca el proyecto con el mismo nombre
        """
        from models import Proyecto
        return Proyecto.query.filter(Proyecto.nombre == nombre).first_or_404()

    def estado(self, nombre, estadoNew):
        """ 
        Guarda el nuevo estado del usuario
        @nombre filtra en funcion al nombre
        @estadoNew asigna el nuevo estado al usuario con ese nombre
        """
        from models import Proyecto
        proyecto = Proyecto.query.filter(Proyecto.nombre == nombre).first_or_404()
        proyecto.estado = estadoNew        
        db.session.commit()
    
    def asignarFase(self, nombre, fase):
        from models import Proyecto, Fase
        proyecto = Proyecto.query.filter(Proyecto.nombre == nombre).first_or_404()
        proyecto.listafases.append(fase)
        db.session.commit()
        
    def asignarLider(self, nombre, nombreLider):
        """
        Asigna un lider a un proyecto 
        @param nombre corresponde al nombre del proyecto
        @param nombreLider corresponde al nombre del usuario que sera lider del proyecto
        """
        from models import Proyecto, Rol , User
        from mgrProyectoXUser import MgrProyectoXUser
        from mgrUserXRol import MgrUserXRol
        from mgrRol import MgrRol
        # se crea el rol lider de proyecto 
        nombreRol = "liderDeProyecto"+"-"+nombre+"-"+nombreLider
        rol = Rol(nombreRol, "se asigno un lider al proyecto ",nombre)
        MgrRol().guardar(rol)
        # asigna el rol al usuario
        MgrUserXRol().guardar(nombreLider, nombreRol) 
        # asigna al proyecto el usuario 
        #MgrProyectoXUser().guardarLider(nombre, nombreLider)
        print "nombre del lider" + nombreLider
        print "nombre del proyecto" + nombre
        proyecto = Proyecto.query.filter(Proyecto.nombre == nombre).first_or_404()
        user = User.query.filter(User.name == nombreLider).first_or_404()
        user.listaproyectos.append(proyecto)
        db.session.commit()

    def asignarUsuario(self, nombre,  nameUser, nombreRol, descripcionRol):
        """
        Asigna a un proyecto el usuario con el rol designado
        @param nombre corresponde al nombre del proyecto
        @param nombreUser corresponde al nombre del usuario que sera asignado al proyecto
        @param nombreRol corresponde al nombre del rol que sera asignado al usuario
        """
        from models import Rol
        from mgrProyectoXUser import MgrProyectoXUser
        from mgrUserXRol import MgrUserXRol
        from mgrRol import MgrRol
        # crea el rol
        nombreRol = nombreRol+"-"+nombre+"-"+nameUser
        rol = Rol(nombreRol, descripcionRol,nombre)
        MgrRol().guardar(rol)
        # asigna el rol al usuario
        MgrUserXRol().guardar(nameUser, nombreRol) 
        # asigna al proyecto el usuario 
        MgrProyectoXUser().guardar(nombre, nameUser)

    
    
    def desasignarUsuario(self, nombre,  nameUser, nombreRol):
        """
        Desasigna a un proyecto el usuario con el rol designado
        @param nombre corresponde al nombre del proyecto
        @param nombreUser corresponde al nombre del usuario que sera asignado al proyecto
        @param nombreRol corresponde al nombre del rol que sera asignado al usuario
        """
        from models import Rol
        from mgrProyectoXUser import MgrProyectoXUser
        from mgrUserXRol import MgrUserXRol
        from mgrRol import MgrRol
        # desasigna el rol al usuario
        MgrUserXRol().borrar(nameUser, nombreRol) 
        # deasigna del proyecto el usuario 
        MgrProyectoXUser().borrar(nombre, nameUser)
        # borrar el rol
        MgrRol().borrar(nombreRol)

    def usersDeProyecto(self, nombre):
        from models import Proyecto
        proyecto = Proyecto.query.filter(Proyecto.nombre == nombre).first_or_404()
        return proyecto.users
    
    def liderProyecto(self, nombre):
        from models import Proyecto
        from models import User
        proyecto = Proyecto.query.filter(Proyecto.nombre == nombre).first_or_404()
        liderid = proyecto.lider
        lider = User.query.filter(User.idUser == liderid).first_or_404()
        return lider
    
    def filtrarFases(self, nombre):
        """ filtrar items por nombre """
        from models import Proyecto
        from models import Fase
        proyecto = Proyecto.query.filter(Proyecto.nombre == nombre).first_or_404()
        return proyecto.listafases

        