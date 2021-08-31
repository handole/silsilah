from sanic import Sanic
from sanic.response import json
from sanic_cors import CORS, cross_origin
from sanic_openapi import swagger_blueprint
import psycopg2
import psycopg2.extras

app = Sanic(__name__)
CORS(app)
app.blueprint(swagger_blueprint)
connection = None
cursor = None
curfunc = None

def connect():
    try:
        connection = psycopg2.connect(host="127.0.0.1",
            user="postgres",
            password="020",
            port="5432",
            database="keluarga")
        connection.autocommit = True

    except (Exception, psycopg2.DatabaseError) as error:
        return error
    finally:
        return connection

@app.route("/test", methods=['GET'])
async def test(request):
    return json({"Status": "Sukses"})

@app.route("/list", methods=['GET'])
async def list(request):
    connection = connect()
    curfunc = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    try:
        sql = "SELECT * FROM silsilah"
        curfunc.execute(sql)
        row = curfunc.fetchall()
        data = []
        for i in row:
            id = int(i[0])
            name = str(i[1])
            gender = str(i[2])
            status = str(i[3])

            data.append({
                "id": id,
                "name": name,
                "gender": gender,
                "status": status
            })
        return json({"rows": data}, 200)
    except Exception as err:
        return json({"Status": "Failed"}, 500)

@app.route("/anak", methods=['GET'])
async def anak(request):
    connection = connect()
    curfunc = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    try:
        sql = "SELECT * FROM silsilah WHERE status='Anak'"
        curfunc.execute(sql)
        row = curfunc.fetchall()
        data = []
        for i in row:
            id = int(i[0])
            name = str(i[1])
            gender = str(i[2])
            status = str(i[3])

            data.append({
                "id": id,
                "name": name,
                "gender": gender,
                "status": status
            })
        return json({"rows": data}, 200)
    except Exception as err:
        return json({"Status": "Failed"}, 500)

@app.route("/cucu", methods=['GET'])
async def cucu(request):
    connection = connect()
    curfunc = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    try:
        sql = "SELECT * FROM silsilah WHERE status='Cucu'"
        curfunc.execute(sql)
        row = curfunc.fetchall()
        data = []
        for i in row:
            id = int(i[0])
            name = str(i[1])
            gender = str(i[2])
            status = str(i[3])

            data.append({
                "id": id,
                "name": name,
                "gender": gender,
                "status": status
            })
        return json({"rows": data}, 200)
    except Exception as err:
        return json({"Status": "Failed"}, 500)

@app.route("/cucu/perempuan", methods=['GET'])
async def cucu_perempuan(request):
    connection = connect()
    curfunc = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    try:
        sql = "SELECT * FROM silsilah WHERE status='Cucu' AND gender='perempuan'"
        curfunc.execute(sql)
        row = curfunc.fetchall()
        data = []
        for i in row:
            id = int(i[0])
            name = str(i[1])
            gender = str(i[2])
            status = str(i[3])

            data.append({
                "id": id,
                "name": name,
                "gender": gender,
                "status": status
            })
        return json({"rows": data}, 200)
    except Exception as err:
        return json({"Status": "Failed"}, 500)

@app.route("/bibi", methods=['GET'])
async def bibi(request):
    connection = connect()
    curfunc = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    try:
        sql = "SELECT * FROM silsilah WHERE status='Anak' AND gender='perempuan'"
        curfunc.execute(sql)
        row = curfunc.fetchall()
        data = []
        for i in row:
            id = int(i[0])
            name = str(i[1])
            gender = str(i[2])
            status = str(i[3])

            data.append({
                "id": id,
                "name": name,
                "gender": gender,
                "status": status
            })
        return json({"rows": data}, 200)
    except Exception as err:
        return json({"Status": "Failed"}, 500)

@app.route("/sepupu/laki-laki", methods=['GET'])
async def sepupu_laki(request):
    connection = connect()
    curfunc = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    try:
        sql = "SELECT * FROM silsilah WHERE status='Cucu' AND gender='laki-laki'"
        curfunc.execute(sql)
        row = curfunc.fetchall()
        data = []
        for i in row:
            id = int(i[0])
            name = str(i[1])
            gender = str(i[2])
            status = str(i[3])

            data.append({
                "id": id,
                "name": name,
                "gender": gender,
                "status": status
            })
        return json({"rows": data}, 200)
    except Exception as err:
        return json({"Status": "Failed"}, 500)


@app.route("/nambah/anak", methods=['POST'])
async def nambah_anak(request):
    try:
        body = request.json
    except Exception as err:
        print(err)
        return json({"Status": "Bad Request"}, 400)

    connection = connect()
    curfunc = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    try:
        name = body.get("name")
        gender = body.get("gender")

        sql = "INSERT INTO silsilah(name, gender, status) VALUES('"+str(name)+"', '"+str(gender)+"','Anak')"
        curfunc.execute(sql)
        return json({"status": "Insert data success"})
    except Exception as err:
        return json({"Status": "Failed"}, 500)
    
@app.route("/nambah/cucu", methods=['POST'])
async def nambah_cucu(request):
    try:
        body = request.json
    except Exception as err:
        print(err)
        return json({"Status": "Bad Request"}, 400)

    connection = connect()
    curfunc = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    try:
        name = body.get("name")
        gender = body.get("gender")

        sql = "INSERT INTO silsilah(name, gender, status) VALUES('"+str(name)+"', '"+str(gender)+"','Cucu')"
        curfunc.execute(sql)
        return json({"status": "Insert data success"})
    except Exception as err:
        return json({"Status": "Failed"}, 500)

@app.route("/edit/<int:id>", methods=['POST'])
async def edit(request, id):
    try:
        body = request.json
    except Exception as err:
        print(err)
        return json({"Status": "Bad Request"}, 400)

    connection = connect()
    curfunc = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    try:
        name = body.get("name")
        gender = body.get("gender")
        status = body.get("status")

        sql = "UPDATE silsilah SET name='"+str(name)+"', gender='"+str(gender)+"', status='"+str(status)+"' WHERE id='"+id+"'"
        curfunc.execute(sql)
        return json({"status": "Update data success"})
    except Exception as err:
        return json({"Status": "Failed"}, 500)

@app.route("/delete/<int:id>", methods=['POST'])
async def delete(request, id):
    try:
        body = request.json
    except Exception as err:
        print(err)
        return json({"Status": "Bad Request"}, 400)

    connection = connect()
    curfunc = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    try:
        sql = "DELETE FROM silsilah WHERE id={}".format(id)
        curfunc.execute(sql)
        return json({"status": "Delete data success"})
    except Exception as err:
        return json({"Status": "Failed"}, 500)

if __name__ == "__main__":
    app.run(debug=True)
    # app.run(host="0.0.0.0", port=8000)