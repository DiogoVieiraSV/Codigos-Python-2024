def converter(temperatura_celsius):
    """Converte a temperatura de Celsius para Fahrenheit."""
    temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32
    return temperatura_fahrenheit

# Exemplo de uso
temperatura = float(input("Digite a temperatura em Celsius: "))
resultado = converter(temperatura)
print(f"A temperatura em Fahrenheit é: {resultado:.2f}°F")