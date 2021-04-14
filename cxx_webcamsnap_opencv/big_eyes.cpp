#include <iostream>
#include <opencv2/opencv.hpp>
//#include <opencv2/core.hpp>
//#include <opencv2/videoio.hpp>
//#include <opencv2/highgui.hpp>
#include <unistd.h>
// compile : g++ big_eyes.cpp -I/usr/include -L/usr/lib/ -lopencv_core -lopencv_cvv -lopencv_highgui -lopencv_videoio -lopencv_imgcodecs -o lol

using namespace std;
using namespace cv;

int main()
{
    Mat frame;
    VideoCapture cap;
    cap.open(0);

    int deviceID = 0;
    int apiID = cv::CAP_ANY;

    cap.open(deviceID + apiID);

    if (!cap.isOpened())
    {
        cerr << "[+] Error Camera not opened !" << endl;
        return -1;
    }
    cout << "Start Grabbing" << endl;
    for (;;)
    {
        cap.read(frame);

        if (frame.empty())
        {
            cerr << "[!] Frame is empty " << endl;
            break;
        }

        sleep(3);
        imwrite("frame.jpg",frame);
        break;
    }
    return 0;
}
