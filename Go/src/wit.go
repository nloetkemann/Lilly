package src

import (
	"os"
	"fmt"

	witai "github.com/wit-ai/wit-go"
)
var Client = witai.NewClient(os.Getenv("WIT_TOKEN"))



func Send_2_wit(c chan int, audioFileName string) {
	fmt.Println(Client.Export())
	file, _ := os.Open(audioFileName)

	msg, error := Client.Speech(&witai.MessageRequest{
		Speech: &witai.Speech{
			File:        file,
			ContentType: "audio/raw;encoding=unsigned-integer;bits=16;rate=16k;endian=little",
		},
	})
	// msg, error := Client.Parse(&witai.MessageRequest{
	// 	Query: "hallo",
	// })

	close(c)
	if error != nil {
		fmt.Println(error)
	}

	fmt.Printf("%v", msg)
}
