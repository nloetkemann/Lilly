package src

import (
	"os"
	"fmt"

	witai "github.com/wit-ai/wit-go"
)
var client = witai.NewClient(os.Getenv("WIT_TOKEN"))


func Send_2_wit(c chan int, audioFileName string) {
  file, _ := os.Open(audioFileName)
  msg, error := client.Speech(&witai.MessageRequest{
  	Speech: &witai.Speech{
  		File:        file,
  		ContentType: "audio/raw;encoding=unsigned-integer;bits=16;rate=16k;endian=little",
  	},
  })
	close(c)
	if error != nil {
		fmt.Println(error)
	}

  fmt.Println(msg.ID)
}
