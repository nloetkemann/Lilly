package main
import "./src"


// stackoverflow.com/questions/14094190/golang-function-similar-to-getchar


func main() {
	// src.Voice_2_text()
	c := make(chan int)
	go src.Send_2_wit(c, "sounds/temp.wav")
	<-c
}
