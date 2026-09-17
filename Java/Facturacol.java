import java.util.Scanner;

public class Facturacol {

    public static void main(String[] args) {
        // Objeto para capturar entradas desde la consola
        Scanner teclado = new Scanner(System.in);

        // Variables principales
        double totalPedido = 0.0;

        // 1. Entradas iniciales
        System.out.print("Ingrese número o nombre de la mesa: ");
        String numMesa = teclado.nextLine();

        System.out.print("Ingrese el nombre del cliente: ");
        String nombreCliente = teclado.nextLine();

        System.out.print("¿Cuántos productos registrará?: ");
        int cantProductos = teclado.nextInt();
        teclado.nextLine(); // Limpiar el buffer de entrada

        // Estructura para almacenar el detalle visual de los productos
        String detalleProductos = "";

        // 2. Bucle para procesar cada producto
        for (int i = 1; i <= cantProductos; i++) {
            System.out.println("\n--- Producto " + i + " ---");
            System.out.print("Nombre del producto: ");
            String nombreProducto = teclado.nextLine();

            System.out.print("Precio unitario: $");
            double precio = teclado.nextDouble();

            System.out.print("Cantidad: ");
            int cantidad = teclado.nextInt();
            teclado.nextLine(); // Limpiar buffer

            // Operaciones aritméticas requeridas
            double subtotal = precio * cantidad;
            totalPedido += subtotal;

            // Formatear línea para el recibo final
            detalleProductos += String.format(" %-18s x%-3d  $%10.2f\n", nombreProducto, cantidad, subtotal);
        }

        // 3. Salida decorada de la factura / recibo
        System.out.println("\n");
        System.out.println("==========================================");
        System.out.println("            FACTURACOL - RESTAURANTE       ");
        System.out.println("==========================================");
        System.out.printf(" Mesa: %-15s Cliente: %-10s\n", numMesa, nombreCliente);
        System.out.println("------------------------------------------");
        System.out.println(" Cant. Producto              Subtotal     ");
        System.out.println("------------------------------------------");
        System.out.print(detalleProductos);
        System.out.println("------------------------------------------");
        System.out.printf(" TOTAL A PAGAR:              $%10.2f\n", totalPedido);
        System.out.println("==========================================");
        System.out.println("   ¡Gracias por su compra, vuelva pronto! ");
        System.out.println("==========================================");

        teclado.close();
    }
}
