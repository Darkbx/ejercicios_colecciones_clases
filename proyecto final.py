def lista_amort():
    class prestamos():
        """CANTIDAD"""
        prestamo = float(input("Cuanto dinero necesita?\n"))
        """PLAZO"""
        plazos = int(input("En cuantos plazos pagara?\n"))
        """INTERES A PAGAR"""
        interes_Pago = float(input("Cantidad de interes que desee pagar?\n"))
        interes_Pago = (interes_Pago / 12) / 100
        """OPERACION"""
        cuota = interes_Pago / ((((1 + interes_Pago) ** -plazos) - 1) * -1)
        cuota = cuota * prestamo
        monto = prestamo
        """AMORTIZACION"""
        CU_OTA = "{0:.2f}".format(cuota)
        print("<-------------------------------------->")
        print("<------------AMORTIZACION-------------->")
        print("<-------------------------------------->")
        """"""
        print("\nPago:0/Plazos:0/Interes:0/Abono:0/Prestamo:{0}\n".format(monto))
        for x in range(1, plazos + 1):
            Interes = "{0:.2f}".format(float(monto) * float(interes_Pago))
            pago = "{0:.2f}".format(float(CU_OTA) - float(Interes))
            monto = "{0:.2f}".format(float(monto) - float(pago))

            if monto < str(0):
                print("Has completado tu prestamo. \n")

            print(
                "Pago:{0} || Plazos:{1} || Interes:{2} || Abono:{3} || Prestamo:{4}\n".format(x, CU_OTA, Interes, pago,
                                                                                        monto))

        print("Fin de la amortizacion")

lista_amort()