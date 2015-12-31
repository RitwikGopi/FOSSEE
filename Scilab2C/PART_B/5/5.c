#include <avr/io.h>
#define F_CPU 8000000

main(){
	DDRD |= (1 << 5);
	TCCR1A |= (1 << COM1A1) | (1 << WGM11);
	TCCR1B |= (1 << WGM13) | (1 << WGM12) | (1 << CS11);
	ICR1 = 499;
	OCR1A = 250;
	while(1);
}
