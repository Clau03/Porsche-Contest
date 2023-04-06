#include "httplib.h"
#include <iostream>
#include <fstream>

using namespace std;
void down_model(){
    httplib::Client cli("http://185.187.169.44:10073");
    cli.set_basic_auth("team4", "MUnFEnRqzH4fBWRT8YXJ");
    auto res = cli.Get("/team4?modelName=my_model.h5");
    
    //cout<<res->body;
    if (res && res->status == 200) {
        // Save the response body to a file
        std::ofstream file("/home/rpy/my_model.h5", std::ios::binary);
        file.write(res->body.c_str(), res->body.size());
        file.close();
    } else {
        std::cout << "Error: " << res.error() << std::endl;
    }
    
}



void upload_result() {
    // Create the client and set the authentication headers
    httplib::Client cli("http://185.187.169.44:10073");
    cli.set_basic_auth("team4", "MUnFEnRqzH4fBWRT8YXJ");

    // Open the file and read the contents into a string
    std::ifstream file("/home/rpy/result.txt");
    std::stringstream buffer;
    buffer << file.rdbuf();
    std::string file_contents = buffer.str();

    // Send the file to the server
    auto res = cli.Post("/team4?uploadResults", file_contents, "application/json");

    // Check the response and print any errors
    if (res && res->status == 200) {
        std::cout << "Result uploaded successfully!" << std::endl;
    } else {
        std::cout << "Error uploading result: " << res->status <<res->body<< std::endl;
    }
}


