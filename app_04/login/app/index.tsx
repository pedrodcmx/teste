import { View, Text, StyleSheet, Image } from 'react-native';
import { Input }
    from '@/components/input'; 
export default function Index(){
    return(
        <View style={style.container}>
            <Image source={require("@/assets/senai.png")} />
            <Text style={style.titulo}>Login</Text>
            <Input placeholder='E-mail' keyboardType='email-address'/>
            <Input placeholder='Senha' secureTextEntry />
        </View>
    )
}
const style = StyleSheet.create({
    container: {
        flex: 1,
        padding: 32
    },
    titulo: {
        fontSize: 32,
        fontWeight: 900
    },
    img: {
        width: '100%'
    }
})