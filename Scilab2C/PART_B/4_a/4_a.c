#include <avr/io.h>
#define F_CPU 1000000

main(){
	DDRC &= ~(1<<0);
	PORTC |= (1<<0);
	DDRB |= (1<<0);
	while(1)
		PORTB = (1<<0) & PINC;
}
