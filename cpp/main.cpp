#include <iostream>
#include <cmath>
#include <iomanip>

int main(){
    // Variable Declarations
    std::string name;
    double height;
    double weight;
    double bmi;

    // User Inputs
    std::cout << "What should I call you?: ";
    getline(std::cin, name);

    std::cout << "Alright " << name << ", what is your height in cms?: ";
    std::cin >> height;
    height = height / 100;
    
    std::cout << "One last question, what is your weight in kgs?: ";
    std::cin >> weight;

    // Calculating BMI
    bmi = weight / (height * height);

    // Output
    std::cout << "You BMI is " << bmi << " kg/m²" << '\n';

    // Categorization
    if(bmi < 18.5){
        std::cout << "You are Underweight" << '\n';
    } else if(bmi < 25){
        std::cout << "You are Healthy Weight" << '\n';
    } else if(bmi < 30){
        std::cout << "You are Overweight" << '\n';
    } else if(bmi >= 30){
        std::cout << "You are Obese" << '\n';
    }

    return 0;
}