import mysql.connector

class Conectar():

    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = 'Vero2003@',
                db = 'db_inm_brf'

            )
        except mysql.connector.Error as  descripcionError:
            print("¡ No se conecto a la Base de Datos",descripcionError)

#-- Listado de propiedades TOTALES, sin distinción de estados --#
            
    def ListarPropiedades(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("select pr.Id_Propiedad, pr.Direccion_Propiedad, pr.Localidad, pr.Provincia, ti.Nombre_Tipo from db_inm_brf.`Propiedad` as pr inner join db_inm_brf.`tipo` as ti on  pr.Id_Tipo = ti.Id_Tipo order by pr.Id_Propiedad")
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados
            
            except mysql.connector.Error as  descripcionError:
                print("¡ No se conecto a la Base de Datos",descripcionError)
                

#-- Listado de propiedades DISPONIBLES para la venta --# 
                
    def ListarPropiedadesDisponiblesVenta(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("select pr.Id_Propiedad, pr.Direccion_Propiedad, es.Nombre_Estado, op.Nombre_Operatoria_Comercial from db_inm_brf.`Propiedad` as pr inner join db_inm_brf.`Estado` as es on  pr.Id_Estado = es.Id_Estado inner join db_inm_brf.`operatoria comercial` as op on pr.Id_Operacion_Comercial = op.Id_Operatoria_Comercial where op.Id_Operatoria_Comercial = 1 and es.Id_Estado = 1 order by pr.Id_Propiedad;")
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados

            except mysql.connector.Error as  descripcionError:
                print("¡ No se conecto a la Base de Datos",descripcionError)


#-- Listado de propiedades DISPONIBLES para alquiler --#
                
    def ListarPropiedadesDisponiblesAlquiler(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("select pr.Id_Propiedad, pr.Direccion_Propiedad, es.Nombre_Estado, op.Nombre_Operatoria_Comercial from db_inm_brf.`Propiedad` as pr inner join db_inm_brf.`Estado` as es on  pr.Id_Estado = es.Id_Estado inner join db_inm_brf.`operatoria comercial` as op on pr.Id_Operacion_Comercial = op.Id_Operatoria_Comercial where op.Id_Operatoria_Comercial = 2 and es.Id_Estado = 1 order by pr.Id_Propiedad;")
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados

            except mysql.connector.Error as  descripcionError:
                print("¡ No se conecto a la Base de Datos",descripcionError)


#-- Listado de propiedades vendidas --#
                
    def ListarPropiedadesVendidas(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("select pr.Id_Propiedad, pr.Direccion_Propiedad, es.Nombre_Estado, op.Nombre_Operatoria_Comercial from db_inm_brf.`Propiedad` as pr inner join db_inm_brf.`Estado` as es on  pr.Id_Estado = es.Id_Estado inner join db_inm_brf.`operatoria comercial` as op on pr.Id_Operacion_Comercial = op.Id_Operatoria_Comercial where op.Id_Operatoria_Comercial = 1 and es.Id_Estado = 2 order by pr.Id_Propiedad;")
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados

            except mysql.connector.Error as  descripcionError:
                print("¡ No se conecto a la Base de Datos",descripcionError)


#-- Listado de propiedades alquiladas --#
                
    def ListarPropiedadesAlquiladas(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("select pr.Id_Propiedad, pr.Direccion_Propiedad, es.Nombre_Estado, op.Nombre_Operatoria_Comercial from db_inm_brf.`Propiedad` as pr inner join db_inm_brf.`Estado` as es on  pr.Id_Estado = es.Id_Estado inner join db_inm_brf.`operatoria comercial` as op on pr.Id_Operacion_Comercial = op.Id_Operatoria_Comercial where op.Id_Operatoria_Comercial = 2 and es.Id_Estado = 2 order by pr.Id_Propiedad;")
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados

            except mysql.connector.Error as  descripcionError:
                print("¡ No se conecto a la Base de Datos",descripcionError)

####################################################################################################################

#-- Listado de Tipos de Propiedades --#
            
    def ListarTipoPropiedad(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM db_inm_brf.tipo")
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados
            
            except mysql.connector.Error as  descripcionError:
                print("¡ No se conecto a la Base de Datos",descripcionError)


#-- Listado de Operatoria Comercial --#
            
    def ListarOperatoriaComercial(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM db_inm_brf. `operatoria comercial`")
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados
            
            except mysql.connector.Error as  descripcionError:
                print("¡ No se conecto a la Base de Datos",descripcionError)                

#-- Listado de Propietarios --#
            
    def ListarPropietarios(self):
        
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM db_inm_brf.propietario")
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados
            
            except mysql.connector.Error as  descripcionError:
                print("¡ No se conecto a la Base de Datos",descripcionError)                

####################################################################################################################
  
    def InsertarPropiedad(self,propiedad):
        con = Conectar()
        if con.conexion.is_connected():
            try:
                cursor = con.conexion.cursor()
                sentenciaSQL = "INSERT INTO db_inm_brf.propiedad (Id_Propiedad, Id_Tipo, Id_Estado, Id_Operacion_Comercial, Id_Propietario, Direccion_Propiedad, Localidad, Provincia) VALUES (null,%s,%s,%s,%s,%s,%s,%s)"

                data = (propiedad.getId_Tipo(),                    
                propiedad.getId_Estado(),
                propiedad.getId_Operacion_Comercial(),
                propiedad.getId_Propietario(),
                propiedad.getDireccion_Propiedad(),
                propiedad.getLocalidad(),
                propiedad.getProvincia())   
                
#                print(data)
#                print(sentenciaSQL)
                
                cursor.execute(sentenciaSQL,data)
#                print(cursor.execute)
                
                con.conexion.commit()
                con.conexion.close()
                print()
                print("===== ¡Propiedad Insertada Correctamente! =====")
                print()

            except mysql.connector.Error  as descripcionError:
                print("¡NO se conectó!",descripcionError)

                
####################################################################################################################
    def ActualizarPropiedad(self,propiedad):
        con = Conectar()
        if con.conexion.is_connected():
            try:
                cursor = con.conexion.cursor()
                sentenciaSQL = "UPDATE db_inm_brf.propiedad SET `Id_Estado` = '%s' WHERE (`Id_Propiedad` = '%s');"

                data = (propiedad.getId_Propiedad(),                    
                propiedad.getId_Estado())   
                
#                print(data)
#                print(sentenciaSQL)
                
                cursor.execute(sentenciaSQL,data)
#                print(cursor.execute)
                
                con.conexion.commit()
                con.conexion.close()
                print()
                print("===== ¡Propiedad Actualizada Correctamente! =====")
                print()

            except mysql.connector.Error  as descripcionError:
                print("¡NO se conectó!",descripcionError)


##########################################################################################################################################################################################################################
                
    def EliminarPropiedad(Id_Propiedad):
        con = Conectar()
        if con.conexion.is_connected():
            try:
                cursor = con.conexion.cursor()
                sentenciaSQL = "DELETE FROM db_inm_brf.propiedad WHERE Id_Propiedad = %s"

                cursor.execute(sentenciaSQL, (Id_Propiedad,))

                con.conexion.commit()
                con.conexion.close()
                print("Propiedad eliminada correctamente")               
            except mysql.connector.Error  as descripcionError:
                print("¡NO se conectó!",descripcionError)
                
####################################################################################################################
               
class propiedad():
    def __init__(self,Id_Propiedad,Id_Tipo,Id_Estado,Id_Operacion_Comercial,Id_Propietario,Direccion_Propiedad,Localidad,Provincia) -> None:
        self.Id_Propiedad = Id_Propiedad
        self.Id_Tipo = Id_Tipo
        self.Id_Estado = Id_Estado
        self.Id_Operacion_Comercial = Id_Operacion_Comercial
        self.Id_Propietario = Id_Propietario
        self.Direccion_Propiedad = Direccion_Propiedad        
        self.Localidad = Localidad
        self.Provincia = Provincia

    def getId_Propiedad(self):
        return self.Id_Propiedad
    def getId_Tipo(self):
        return self.Id_Tipo
    def getId_Estado(self):
        return self.Id_Estado
    def getId_Operacion_Comercial(self):
        return self.Id_Operacion_Comercial
    def getId_Propietario(self):
        return self.Id_Propietario
    def getDireccion_Propiedad(self):
        return self.Direccion_Propiedad
    def getLocalidad(self):
        return self.Localidad
    def getProvincia(self):
        return self.Provincia

    def setId_Propiedad(self,Id_Propiedad):
        self.Id_Propiedad = Id_Propiedad
    def setId_Tipo(self, Id_Tipo):
        self.Id_Tipo = Id_Tipo
    def setId_Estado(self, Id_Estado):
        self.Id_Estado = Id_Estado
    def setId_Operacion_Comercial(self, Id_Operacion_Comercial):
        self.Id_Operacion_Comercial = Id_Operacion_Comercial
    def setId_Propietario(self, Id_Propietario):
        self.Id_Propietario = Id_Propietario
    def setDireccion_Propiedad(self, Direccion_Propiedad):
        self.Direccion_Propiedad = Direccion_Propiedad
    def setLocalidad(self, Localidad):
        self.Localidad = Localidad
    def setProvincia(self, Provincia):
        self.Provincia = Provincia

    def __str__(self) -> str:
        return str(self.Id_Propiedad) + ' ' + str(self.Id_Tipo) +' ' + str(self.Id_Estado) +' ' + str(self.Id_Operacion_Comercial) +' ' + str(self.Id_Propietario) +' ' + str(self.Direccion_Propiedad) +' ' + str(self.Localidad) +' ' + str(self.Provincia)

    

#con = Conectar()
#con.InsertarPropiedad(1,1,1,1,'o','oo','ooo')
#con = Conectar()
#con.EliminarPropiedad(21)


        