#Perdon por el Ingles pero me acostumbre a escribir el codigo asi jaja 
"""
PERDON POR LOS PRINT pero estaba aburrido y quize joder con eso un rato

Me piden una clase que tenga funciones de crud por lo que veo y pues que
la estructura del json sea nombre,apellido,edad,mail y tambien un id porque sino como se va a borrar y editar jajakjska


https://www.youtube.com/watch?v=ekaIEZHJXd4



Les explico en que consiste 4 funciones, una crea, otra borra por medio de ID, otra edita por medio de ID y la otra lista en general



"""

import json

class user_modification:

    def __init__(self,name,lastname,age,mail,id):

        self.id=id
        self.name=name
        self.lastname=lastname
        self.age=age 
        self.mail=mail  

    def save_data(self,name,lastname,age,mail,id):
        try:
            with open("assets\\data.json","r+") as outfile:
                new_insert={
                "name":name if len(name)>0 else "el guevon no quiso poner nombre"
                ,"age":"no quizo poner la edad" if type(age).__name__=="int" else age,
                "lastname":lastname,
                "mail":mail,
                "id":id
                }
                file_dat=json.load(outfile)
                file_dat.append(new_insert)
                outfile.seek(0)
                json.dump(file_dat,outfile,indent=4)

            print( "Exito, Alkosto, Olimpica, D1 :)")
            outfile.close()
        except:
            print("este marica no puso nada")

    def delete_data(self,id):
        
        obj  = json.load(open("assets\\data.json"))
        if len(obj):
            for i in range(len(obj)):
                if obj[i]["id"] == id:
                    obj.pop(i)
                    break
            open("assets\\data.json", "w").write(
        json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': '))
                    )
            print("Se saco de la nomina al fulano porque no servia pa ni chimba")
        print("relajase ome que ya borraste todo")
    
    def see_data(self):
        obj=json.load(open("assets\\data.json"))
        if len(obj):
            return '\n'.join(str(i) for i in obj)
        print("NO Hay nada porque a un genio le dio por borrar todo lo que tenia el json :( ")

    def edit_data(self,id,name,lastname,email,age):
        try:
            obj  = json.load(open("assets\\data.json"))
            if len(obj):
                for i in range(len(obj)):
                    if obj[i]["id"] == id:
                        obj[i]["name"]=name
                        obj[i]["email"]=email
                        obj[i]["age"]=age
                        obj[i]["lastname"]=lastname
                        break
                open("assets\\data.json", "w").write(json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': ')))
                print("Si Cñor has sido actualizadooooooo")
        except:
            print("oee pero ponga los argumentos en orden jajajaja")




user=user_modification("name","last","age","mail","id")


#Crear datos por medio de insercciones en funciones
user.save_data("trabajora","raudal",35,"raudal.castellana@mileroticos.com","12323")

#Eliminar datos por medio de parametros en las funciones de la clase :)
user.delete_data("1")


#Editar datos por medio de parametros en las funciones de la clase
user.edit_data("1","careverga","apellido","estamuycuchalahp@mileroticos.com",45)


#Este print si lo puse para que miraran los datos
print(user.see_data())

    