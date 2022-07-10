#include <iostream>
#include <iomanip>
#include <vector>
#include <fstream>
using namespace std;
int main(int argc, char **argv)
{
    int fn = 1; // file number counter

    ifstream file; // input file reading
    ostringstream ostr;

    // array of voltages and currents
    vector<float> vol; 
    vector<float> curr;

    // array of the forming  voltages
    vector<float> fv;

    float num;

    // logic to open each file
    string input_file;
    ostr << "device-" << setw(2) << setfill('0') << fn << "-meas-01.txt";
    input_file = argv[1];
    input_file += "\\" + ostr.str();
    ostr.clear();
    ostr.str("");


    //file with every forming volatge listed
    string output_file = "formingvoltage.txt";

    while (true)
    {
        file.open(input_file); //open file
        
        if (file.fail()) // file doesn't exist break loop (assuming at the end of all files)
        {
            cout << "couldn't open " + input_file << endl;
            break;
        }
        cout << input_file << endl; //output current file name
        
        // transer file data to arrays
        while (file >> num)
        {
            vol.push_back(num);
            file >> num;
            curr.push_back(num);
        }
        file.close(); //close file
    
        // start from end of array to find where the state changes
        num = curr.at(curr.size() - 1);
        for (int i = vol.size() - 2; i >= 0; i--)
        {
            if (curr.at(i) * 10 < num)
            {
                // print the forming voltage and add to array
                cout << "Forming Voltage: " << vol.at(i + 1) << endl;
                fv.push_back(vol.at(i + 1));
                break;
            }
            num = curr.at(i);
        }

        // open next file
        fn++;
        ostr.str("");
        ostr << "device-" << setw(2) << setfill('0') << fn << "-meas-01.txt";
        input_file = argv[1];
        input_file += "\\" + ostr.str();
        ostr.clear();

        curr.clear();
        vol.clear();
    }

    // save voltages to file
    ofstream myoutput(output_file);
    if(myoutput.is_open()){
        for(int i=0;i<fv.size();i++){
            myoutput<<fv.at(i)<<"\n";
        }
    }
    myoutput.close();
    return 1;
}