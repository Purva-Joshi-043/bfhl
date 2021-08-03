from flask import Flask,jsonify, request

app = Flask(__name__)
@app.route('/bfhl', methods=["GET"])
def hello():
    return("hello world")

@app.route('/bfhl', methods=["POST"])
def bfhl():
        user_id = "purva_joshi_29101999"
        arr = request.get_json()
        arr = arr['numbers']
        try:
            arr = list(map(int,arr))
            is_success = True
            even_arr = []
            odd_arr = []
            for a in arr:
                if a%2 == 0:
                    even_arr.append(a)
                else:
                    odd_arr.append(a)  
            return jsonify(is_success=is_success,user_id=user_id,even=even_arr,odd=odd_arr),200
        except:
            is_success=False
            return jsonify(is_success=is_success,user_id=user_id)  , 400       


    

    



if __name__ == "__main__":
    app.run(port=5000,debug=True)