package src
/*
  #include <stdio.h>
  #include <unistd.h>
  #include <termios.h>
  char getch(){
      char ch = 0;
      struct termios old = {0};
      fflush(stdout);
      if( tcgetattr(0, &old) < 0 ) perror("tcsetattr()");
      old.c_lflag &= ~ICANON;
      old.c_lflag &= ~ECHO;
      old.c_cc[VMIN] = 1;
      old.c_cc[VTIME] = 0;
      if( tcsetattr(0, TCSANOW, &old) < 0 ) perror("tcsetattr ICANON");
      if( read(0, &ch,1) < 0 ) perror("read()");
      old.c_lflag |= ICANON;
      old.c_lflag |= ECHO;
      if(tcsetattr(0, TCSADRAIN, &old) < 0) perror("tcsetattr ~ICANON");
      return ch;
  }
*/
import "C"


import (
	"fmt"
	"github.com/gordonklaus/portaudio"
	wave "github.com/zenwerk/go-wave"
	"math/rand"
	"os"
	"time"
)

func errCheck(err error) {

	if err != nil {
		panic(err)
	}
}


func Voice_2_text() {
  audioFileName := "sounds/temp.wav"

	waveFile, err := os.Create(audioFileName)
	errCheck(err)

	// www.people.csail.mit.edu/hubert/pyaudio/  - under the Record tab
	inputChannels := 1
	outputChannels := 0
	sampleRate := 44100
	framesPerBuffer := make([]byte, 64)

	portaudio.Initialize()
	//defer portaudio.Terminate()

	stream, err := portaudio.OpenDefaultStream(inputChannels, outputChannels, float64(sampleRate), len(framesPerBuffer), framesPerBuffer)
	errCheck(err)
	//defer stream.Close()

	// setup Wave file writer

	param := wave.WriterParam{
		Out:           waveFile,
		Channel:       inputChannels,
		SampleRate:    sampleRate,
		BitsPerSample: 8, // if 16, change to WriteSample16()
	}

	waveWriter, err := wave.NewWriter(param)
	errCheck(err)

	// defer waveWriter.Close()
	// defer portaudio.Terminate()
	// defer stream.Close()

	// go func() {
	// 	time.Sleep(4000 * time.Millisecond)
	// 	fmt.Println("\nCleaning up ...")
	// 	stream.Stop()
	// 	stream.Close()
	// 	c := make(chan int)
	// 	Send_2_wit(c, audioFileName)
	// 	<-c
	// 	os.Exit(0)
	//
	// }()
	go func() {
		time.Sleep(4000 * time.Millisecond)
		fmt.Println()
		fmt.Println("Cleaning up ...")
		waveWriter.Close()
		stream.Close()
		portaudio.Terminate()
		// c := make(chan int)
		// Send_2_wit(c, audioFileName)
		// <-c
		os.Exit(0)
	}()

	// recording in progress ticker. From good old DOS days.
	ticker := []string{
		"-",
		"\\",
		"/",
		"|",
	}
	rand.Seed(time.Now().UnixNano())

	// start reading from microphone
	errCheck(stream.Start())
	for {

		error := stream.Read()
		if error != nil {
			return
		}

		fmt.Printf("\rRecording is live now. Say something to your microphone! [%v]", ticker[rand.Intn(len(ticker)-1)])

		// write to wave file
		_, err := waveWriter.Write([]byte(framesPerBuffer)) // WriteSample16 for 16 bits
		errCheck(err)
	}
	errCheck(stream.Stop())
}
