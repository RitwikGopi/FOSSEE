#include <avr/io.h>
#include <util/delay.h>
#define F_CPU 1000000

main(){
	DDRB = 0xFF;
	PORTB = 0x00;
	DDRC = 0xFF;
	PORTC = 0x00;
	ADCSRA |= (1<<ADEN)|(1<<ADPS2);
	ADMUX |= (1<<REFS0);
	UCSRB |= (1<<TXEN);
	UBRRH = 0x00;
	UBRRL = 0x0C;
	_delay_ms(1);
	while(1){
		int valL,valH;
		ADCSRA |= (1<<ADSC);
		while(ADCSRA & (1<<ADSC));
		valL = ADCL;
		valH = ADCH;
		PORTB = valL;
		PORTC = valH;
		UDR = valL;
		while(!(UCSRA&&(1<<TXC)));
		_delay_ms(1);
		UDR = valH;
		while(!(UCSRA&&(1<<TXC)));
		_delay_ms(1);
	}
}
