package src

import (
	"os"
	"fmt"

	witai "github.com/wit-ai/wit-go"
)
// func init() {
//   var client = witai.NewClient(os.Getenv("WIT_TOKEN"))
// }

var client = witai.NewClient(os.Getenv("WIT_TOKEN"))


func Send_2_wit() {
  file, _ := os.Open("sounds/temp.wav")

  msg, _ := client.Speech(&witai.MessageRequest{
  	Speech: &witai.Speech{
  		File:        file,
  		ContentType: "audio/wav;encoding=unsigned-integer;bits=16;rate=16k;endian=little",
  	},
  })

  fmt.Printf("Return: %f", msg)
}
