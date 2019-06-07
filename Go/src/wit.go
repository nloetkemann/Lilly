package src

import (
	"os"
	"fmt"

	witai "github.com/wit-ai/wit-go"
)

var client = witai.NewClient(os.Getenv("WIT_TOKEN"))


func Send_2_wit(c chan int, audioFileName string) {
  file, _ := os.Open(audioFileName)
	fmt.Println("start sending")
  msg, _ := client.Speech(&witai.MessageRequest{
  	Speech: &witai.Speech{
  		File:        file,
  		ContentType: "audio/wav;encoding=unsigned-integer;bits=16;rate=16k;endian=little",
  	},
  })
	close(c)

  fmt.Printf("Return: %f", msg)
}
