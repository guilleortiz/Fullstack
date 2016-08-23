from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


class WebServerHandler(BaseHTTPRequestHandler):# extiende de BaseHTTPRequestHandler

    def do_GET(self):#determinar el codigo a ejecutar segun la la requesta enviada
       #do_GET se encargar de las requestque nuestro servidad recive
        if self.path.endswith("/hello"):#solo los fijamos en el final de la url
            self.send_response(200)#respuesta  get correcta
            self.send_header('Content-type', 'text/html')#indicamos que respodemos con texto HTMl
            self.end_headers()#envia una linea en blanco para indicar fin de headers
            message = ""
            message += "<html><body>Hello!</body></html>"#lo que respode el server
            self.wfile.write(message)#enviamos el mensaje de nuevo al cliente
            print message
            return

        if self.path.endswith("/hola"):#solo los fijamos en el final de la url
            self.send_response(200)#respuesta  get correcta
            self.send_header('Content-type', 'text/html')#indicamos que respodemos con texto HTMl
            self.end_headers()#envia una linea en blanco para indicar fin de headers
            message = ""
            message += "<html><body>hola!</body></html>"#lo que respode el server
            self.wfile.write(message)#enviamos el mensaje de nuevo al cliente
            print message
            return



        else:
            self.send_error(404, 'File Not Found: %s' % self.path)#si no poen hello al final


def main():#instaciamos el main ademas de indicar el puerto
    try:
        port = 8080
        server = HTTPServer(('', port), WebServerHandler)#instancia de HTTPServer
        print "Web Server running on port %s" % port
        server.serve_forever()#se mantendra constantemente escuchando hasta (ctrl+c)
    except KeyboardInterrupt:# si el evento especificado ocurre(ctrl+c)
        print " ^C entered, stopping web server...."
        server.socket.close()#apagamos el servidor

if __name__ == '__main__':#se ejecutara inmediatamente  el main cuando el itnterpetre ejecute el script
    main()